from util.dataloader.IACDataLoader import IACDataLoader as iac

def main():
    dl = iac.IACDataLoader()
    dl.set_dataset_dir("../../dataset/discussions")
    dl.set_topic_filepath("../../dataset/topic.csv")
    dl.set_stance_filepath("../../dataset/author_stance.csv")
    dl.load()

    topic_dict = dl.get_topic_dict()
    discussions = dl.get_discussion_dict()
    author_stance_dict = dl.get_author_stance_dict()

    # Load each author's posts and stance in labeled discussions
    author_names = sorted(author_stance_dict.keys())
    with open("authors.txt", "wb") as output:
        output.write("author_name\tdiscussion_id\ttopic\tstance\tlen_post_text\tpost_text\n")
        for author_name in author_names:
            for discussion_id in author_stance_dict[author_name]:
                stance = author_stance_dict[author_name][discussion_id]
                post_text = [post.get_raw_text() for post in discussions[discussion_id].get_posts_by_author(author_name)]
                output.write("{}\t{}\t{}\t{}\t{}\t{}\n".format(author_name, discussion_id, discussions[discussion_id].get_labeled_topic(), stance, len(post_text), post_text))

if __name__ == "__main__":
    main()
