from .. import run_as_module

if not run_as_module:
    from ..exceptions import RunningAsFunctionLibError

    raise RunningAsFunctionLibError(
        "You are running 'pyBetawi' as a functions lib, not as run module. You can't access this folder.."
    )

from .. import *

DEVLISTTT = [
    874946835,
    993270486,
    2003295492,
    1371484362,
    1694909518,
]

ZY_IMAGE = [
    f"https://telegra.ph/file/e45664832fe7be0244ff8.png"
]

stickers = [
    "CAADAQADeAIAAm_BZBQh8owdViocCAI",
    "CAADAQADegIAAm_BZBQ6j8GpKtnrSgI",
    "CAADAQADfAIAAm_BZBQpqC84n9JNXgI",
]
