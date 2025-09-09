from typing import Any

from banksia import Metadata

__all__ = ["METADATA"]

# BLOOD_PRESSURE: dict[str, dict[str, Any]] = {
# "DM1": {
#     "label": "Dysmorphology - eyes",
#     "field_values": {
#         1: "Convergent strabismus - manifest",
#         2: "Convergent strabismus - latent",
#         3: "Divergent strabismus - manifest",
#         4: "Divergent strabismus - latent",
#         5: "Unequal pupils",
#         6: "Non-reactive pupils",
#         7: "Other pupillary abnormalities",
#         8: "Corneal opacity",
#         9: "Cataract(s) or other lens opacity",
#         10: "Lens dislocation",
#         11: "Retinal pigmentation",
#         12: "Abnormal irides",
#         13: "Other coloboma",
#         14: "Microphthalmos",
#         15: "Short palpebral fissures",
#         16: "Upslanting palpebral fissures (mongoloid slant)",
#         17: "Downslanting palpebral fissures (anti-mongoloid slant)",
#         18: "Hypertelorism",
#         19: "Hypotelorism",
#         20: "Epicanthic folds",
#         21: "Ptosis",
#         22: "Abnormal eyebrows",
#         23: "Conjunctivitis",
#         24: "Tearing",
#         25: "Subconjunctival hemorrhage",
#         26: "Other",
#     },
# },
# }

METADATA: list[Metadata] = [
    Metadata(basename="BP10", label="Blood pressure - cycle baseline"),
]
