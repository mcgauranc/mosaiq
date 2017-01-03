""" Test Flow Definition"""

from activflow.quotient.models import Sample, FileResult, ManualDataSet
from activflow.quotient.rules import progress, is_conformant, is_non_conformant
ManualDataSet
FLOW = {
    'receive_sample': {
        'name': 'Receive Sample',
        'model': Sample,
        'role': 'Submitter',
        'transitions': {
            'record_pretyping': progress,
        }
    },
    'record_pretyping': {
        'name': 'Record Sample Pre-typing',
        'model': ManualDataSet,
        'role': 'Reviewer',
        'transitions': {
            'import_results': progress,
        }
    },
    'import_results': {
        'name': 'Import Results',
        'model': FileResult,
        'role': 'Submitter',
        'transitions': {
            'final_report': is_conformant,
            'rerun': is_non_conformant,
        }
    },
    'final_report': {
        'name': 'Run Final Report',
        'model': FileResult,
        'role': 'Submitter',
        'transitions': None
    },
    'rerun': {
        'name': 'Import Results (2nd Run)',
        'model': FileResult,
        'role': 'Submitter',
        'transitions': {
            'import_results': progress,
        }
    },
}

INITIAL = 'receive_sample'

TITLE = 'mosaiQ Vaidation'
DESCRIPTION = 'Validation process for mosaiQ'
