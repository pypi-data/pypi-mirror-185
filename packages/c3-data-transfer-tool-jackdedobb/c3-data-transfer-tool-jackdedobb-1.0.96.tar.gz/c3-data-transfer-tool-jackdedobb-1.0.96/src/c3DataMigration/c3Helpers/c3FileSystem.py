__author__ = 'Jackson DeDobbelaere'
__credits__ = ['Jackson DeDobbelaere']
__maintainer__ = 'Jackson DeDobbealere'
__email__ = 'jackson.dedobbelaere@c3.ai'


#!/usr/bin/env python3
import gzip
import json
import os
import shutil
from pathlib import Path
from reprint import output
from c3DataMigration.c3Helpers import c3Request
from c3DataMigration.c3Helpers import c3UtilityMethods




def getRemoteFileSystemInstance (r, p):
  url = c3Request.generateTypeActionURL(r, 'FileSystem', 'inst')
  errorCodePrefix = 'Unsuccessful retrieving instance of FileSystem'
  request = c3Request.makeRequest(r, p.errorSleepTimeSeconds, url, None, errorCodePrefix)
  fileSystemInstance = json.loads(request.text)['type']

  return fileSystemInstance



def getRemoteRootURL (r, p):
  fileSystemInstance = getRemoteFileSystemInstance(r, p)
  url = c3Request.generateTypeActionURL(r, fileSystemInstance, 'rootUrl')
  payload = {
    'this': {}
  }
  errorCodePrefix = 'Unsuccessful root url of FileSystem'
  request = c3Request.makeRequest(r, p.errorSleepTimeSeconds, url, payload, errorCodePrefix)
  rootURL = request.text.replace('"', '')

  return rootURL



def getRemoteImportDirectory (r, p):
  scriptRunnerUsername = c3UtilityMethods.getc3Context(r, p.errorSleepTimeSeconds)['username']
  directoryOnEnv = '/'.join(['c3-cp', 'jack-data-transfer', scriptRunnerUsername]) # TODO: May also want to key off timestamp

  return directoryOnEnv




def deleteRemoteDirectory (r, p, folderPath):
  fileSystemInstance = getRemoteFileSystemInstance(r, p)
  url = c3Request.generateTypeActionURL(r, fileSystemInstance, 'deleteFiles')
  payload = {
    'this': {},
    'urlOrEncodedPath': folderPath,
    'confirm': True,
  }
  errorCodePrefix = 'Unsuccessful cleaning up deleting folder on environment'
  c3Request.makeRequest(r, p.errorSleepTimeSeconds, url, payload, errorCodePrefix)




def deleteRemoteFiles (r, p, filePathList):
  fileSystemInstance = getRemoteFileSystemInstance(r, p)
  url = c3Request.generateTypeActionURL(r, fileSystemInstance, 'deleteFilesBatch')
  payload = {
    'this': {},
    'files': filePathList,
  }
  errorCodePrefix = 'Unsuccessful cleaning up generated files on environment'
  c3Request.makeRequest(r, p.errorSleepTimeSeconds, url, payload, errorCodePrefix)




def deleteLocalFiles (filePaths):
  for filePath in filePaths:
    path = Path(filePath)
    if (path.exists() and path.is_file()):
      os.remove(path)




def wipeLocalDirectory (p, filePath, promptUser=False):
  path = Path(filePath)
  if (path.exists() and path.is_dir()):
    if (promptUser == True):
      string = 'Type (y/yes) to confirm directory removal: ' + filePath
      c3UtilityMethods.printFormatWrapMaxColumnLength(string, p.maxColumnPrintLength, True)
      if (not (input().lower() in ['y', 'yes'])):
        print('Exiting script.')
        exit(0)
    shutil.rmtree(path)
  path.mkdir(parents=True, exist_ok=True)




def getLocalFilePathsWithinDirectory (directory, optionalFileExtension=None):
  fullFilePaths = []
  if (os.path.isdir(directory)):
    fileNames = next(os.walk(directory), (None, None, []))[2]
    fullFilePaths = ['/'.join([directory, x]) for x in fileNames]

    if (optionalFileExtension != None):
      fullFilePaths = [x for x in fullFilePaths if (x.endswith(optionalFileExtension))]

  return fullFilePaths




def readJsonGzipFileContents (fullFilePath):
  records = []
  try:
    with gzip.open(fullFilePath, 'rb') as gzipFile:
      gzipFileContents = gzipFile.read()
      records = json.loads(gzipFileContents.decode('utf-8'))
  except:
    with open(fullFilePath, 'rb') as gzipFile:
      gzipFileContents = gzipFile.read()
      records = json.loads(gzipFileContents.decode('utf-8'))

  if (type(records) == dict):
    records = records['data']

  return records




def writeJsonGzipFileContents (fullFilePath, records, overwriteFile=False):
  mode = 'xb'
  if (overwriteFile == True):
    mode = 'wb'
  with gzip.open(fullFilePath, mode) as gzipFile:
    gzipFile.write(json.dumps(records, sort_keys=True, indent=2).encode('utf-8'))




def scanFilesInTypeDirectory (r, p, c3Type, filePaths, outputLines):
  def _printHelper (idx, total):
    fileStringPartsStringArr = c3UtilityMethods.printFormatExtraPeriods('Files:', '{:,}'.format(idx), 13, False)
    fileString = fileStringPartsStringArr[0] + (' ' * len(fileStringPartsStringArr[1])) + fileStringPartsStringArr[2]
    totalRecordPartsStringArr = c3UtilityMethods.printFormatExtraPeriods('Records:', '{:,}'.format(total), 19, False)
    totalRecordString = totalRecordPartsStringArr[0] + (' ' * len(totalRecordPartsStringArr[1])) + totalRecordPartsStringArr[2]
    suffixString = fileString + ' / ' +  totalRecordString
    outputLines[-1] = ''.join(c3UtilityMethods.printFormatExtraPeriods('Scanning ' + c3Type, suffixString, p.maxColumnPrintLength, False))

  fieldLabelMap = None
  if (p.stripMetadataAndDerived == True):
    fieldLabelMap = c3UtilityMethods.retrieveLabeledFields(r, c3Type, p.errorSleepTimeSeconds)

  seen, dupes = set(), set()
  total = 0
  _printHelper(0, 0)
  for idx, filePath in enumerate(filePaths):
    if (os.path.exists(filePath) and Path(filePath).is_file()):
      records = readJsonGzipFileContents(filePath)

      total += len(records)
      for x in records:
        if x['id'] in seen:
          dupes.add(x['id'])
        else:
          seen.add(x['id'])

      if (p.stripMetadataAndDerived == True):
        c3UtilityMethods.stripMetaAndDerivedFieldsFromRecords(records, fieldLabelMap)
        writeJsonGzipFileContents(filePath, records, True)

      _printHelper(idx + 1, total)

  return total, list(dupes)




def scanFilesInDirectory (r, p, dataTypes, directory, failScriptIfDuplicates=True):
  with output(output_type='list', initial_len=len(dataTypes), interval=0) as outputLines:
    for dataType in dataTypes:
      c3Type = dataType[0]
      dataTypeFolder = '/'.join([directory, c3Type])
      gzipFilePaths = getLocalFilePathsWithinDirectory(dataTypeFolder, '.gz')

      if (p.outerAPICall == 'uploadAPI'):
        if (dataType[1]['uploadData'] != True):
          outputLines.append(''.join(c3UtilityMethods.printFormatExtraPeriods('Scanning ' + c3Type, 'UPLOAD FLAG IS FALSE', p.maxColumnPrintLength, False)))
          continue
        elif (not os.path.isdir(dataTypeFolder)):
          outputLines.append(''.join(c3UtilityMethods.printFormatExtraPeriods('Scanning ' + c3Type, 'NO IMPORT FOLDER', p.maxColumnPrintLength, False)))
          continue
      elif (p.outerAPICall == 'downloadAPI'):
        if (dataType[1]['downloadData'] != True):
          outputLines.append(''.join(c3UtilityMethods.printFormatExtraPeriods('Scanning ' + c3Type, 'DOWNLOAD FLAG IS FALSE', p.maxColumnPrintLength, False)))
          continue
        elif (not os.path.isdir(dataTypeFolder)):
          outputLines.append(''.join(c3UtilityMethods.printFormatExtraPeriods('Scanning ' + c3Type, 'NO EXPORT FOLDER', p.maxColumnPrintLength, False)))
          continue

      outputLines.append('')
      totalRecordCount, duplicateIds = scanFilesInTypeDirectory(r, p, c3Type, gzipFilePaths, outputLines)

      if ((len(duplicateIds) > 0) and failScriptIfDuplicates):
        string = 'Exiting script. ' + c3Type + ' has duplicate ids: ' + str(duplicateIds)
        errorLines = c3UtilityMethods.printFormatWrapMaxColumnLength(string, p.maxColumnPrintLength, False)
        for errorLine in errorLines:
          outputLines.append(errorLine)
        exit(0)

      dataType[1]['gzipFiles'] = gzipFilePaths
      dataType[1]['recordCount'] = totalRecordCount
