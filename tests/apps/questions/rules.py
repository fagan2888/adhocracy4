import rules

from adhocracy4.modules.predicates import is_allowed_comment_item

rules.add_perm('a4test_questions.comment_question', is_allowed_comment_item)