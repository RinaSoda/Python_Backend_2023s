from datetime import datetime


class Comment:
    def __init__(self, author_id, text):
        self.author_id = author_id
        self.text = text
        self.like_count = 0
        self.create_data = datetime.now()
        self.update_data = self.create_data

    def edit_comment(self, new_text):
        self.text = new_text
        self.update_data = datetime.now()

    def like(self):
        self.like_count += 1

    def dislike(self):
        self.like_count -= 1

    def __repr__(self):
        print('Comment')
        print(f'Author: {self.author_id}')
        print(f'Date: {self.update_data}')
        print(self.text)
        print(f'Likes: {self.like_count}')
        print()
