def filter_comments_by_author(comments, author):
    filtered_comments = []
    for i in range(len(comments)):
        if comments[i].author_id == author.id:
            filtered_comments.append(comments[i])
    return filtered_comments
