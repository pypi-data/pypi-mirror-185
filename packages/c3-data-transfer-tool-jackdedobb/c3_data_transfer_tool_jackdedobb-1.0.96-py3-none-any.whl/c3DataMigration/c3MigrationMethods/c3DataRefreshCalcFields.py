__author__ = 'Jackson DeDobbelaere'
__credits__ = ['Jackson DeDobbelaere']
__maintainer__ = 'Jackson DeDobbealere'
__email__ = 'jackson.dedobbelaere@c3.ai'


#!/usr/bin/env python3
from c3DataMigration.c3Helpers import c3BatchJobs
from c3DataMigration.c3Helpers import c3Queues
from c3DataMigration.c3Helpers import c3Request
from c3DataMigration.c3Helpers import c3UsageStats
from c3DataMigration.c3Helpers import c3UtilityMethods





def _startRefreshCalcFieldsOnEnv (r, p, dataTypes):
  c3TypeToBatchJobMapping = []
  for dataType in dataTypes:
    c3Type = dataType[0]
    if (dataType[1]['refreshCalcFields'] != True):
      c3UtilityMethods.printFormatExtraPeriods('Kicking off ' + c3Type, 'REFRESH FLAG IS FALSE', p.maxColumnPrintLength, True)
      continue

    url = c3Request.generateTypeActionURL(r, c3Type, 'refreshCalcFields')
    errorCodePrefix = 'Unsuccessful kicking off refreshCalcFields of type ' + c3Type
    payload = {
      'spec': {
        'filter':   dataType[1]['filter'] if ('filter' in dataType[1]) else '',
        'async':    True,
        'priority': p.priority,
      }
    }
    errorCodePrefix = 'Unsuccessful getting c3Context'
    request = c3Request.makeRequest(r, p.errorSleepTimeSeconds, url, payload, errorCodePrefix)

    batchJobId = c3BatchJobs.createInitialBatchJobStatusEntry(request, c3Type, c3TypeToBatchJobMapping, None)
    c3UtilityMethods.printFormatExtraPeriods('Kicking off ' + c3Type, 'id=' + str(batchJobId), p.maxColumnPrintLength, True)

  return c3TypeToBatchJobMapping




def _finishRefreshCalcFieldsOnEnv (r, p, c3TypeToBatchJobMapping):
  jobType = 'RefreshCalcFieldsBatchJob'
  c3BatchJobs.waitForBatchJobsToComplete(r, p, c3TypeToBatchJobMapping, jobType, 'refreshCalcs')




def refreshDataOnEnv (r, p, dataTypes):
  if (p.masterRefreshDataSwitch != True):
    return

  c3UtilityMethods.printFormatExtraDashes('REFRESHING CALC FIELDS ON ENV', p.maxColumnPrintLength, True)
  c3TypeToBatchJobMapping = _startRefreshCalcFieldsOnEnv(r, p, dataTypes)
  _finishRefreshCalcFieldsOnEnv(r, p, c3TypeToBatchJobMapping)

  c3UtilityMethods.printFormatExtraDashes('GENERATING CALC FIELDS QUEUE ERROR FILES', p.maxColumnPrintLength, True)
  jobType = 'RefreshCalcFieldsBatchJob'
  c3Queues.outputAllQueueErrorsFromMapping(r, p, c3TypeToBatchJobMapping, jobType)

  if (p.outerAPICall == 'downloadAPI'):
    c3UsageStats.DownloadAPI.logAPIRefreshCalcs(r, p, c3TypeToBatchJobMapping)
  elif (p.outerAPICall == 'uploadAPI'):
    c3UsageStats.UploadAPI.logAPIRefreshCalcs(r, p, c3TypeToBatchJobMapping)
