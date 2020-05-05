from .builtin_rules import vanishing_gradient
from .builtin_rules import all_zero
from .builtin_rules import check_input_images
from .builtin_rules import similar_across_runs
from .builtin_rules import weight_update_ratio
from .builtin_rules import exploding_tensor
from .builtin_rules import unchanged_tensor
from .builtin_rules import loss_not_decreasing
from .builtin_rules import dead_relu
from .builtin_rules import confusion
from .builtin_rules import class_imbalance
from .builtin_rules import confusion
from .builtin_rules import overfit
from .builtin_rules import tree_depth
from .builtin_rules import tensor_variance
from .builtin_rules import overtraining
from .builtin_rules import poor_weight_initialization
from .builtin_rules import saturated_activation
from .builtin_rules import nlp_sequence_ratio

from ._collections import get_collection