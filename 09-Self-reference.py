from typing import List, Optional
from pydantic import BaseModel


class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List['Comment']] = None  # A comment can have a list of replies, which are also Comment instances (self-referential)


Comment.model_rebuild()  # This is necessary to allow for self-referential models in pydantic

comment = Comment(
    id=1,
    content="This is a comment.",
    replies=[
        Comment(id=2, content="This is a reply to the comment."),
        Comment(id=3, content="This is another reply to the comment.")
    ]
)
print(comment)