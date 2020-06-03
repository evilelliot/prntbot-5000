import facebook
from app.crawler import *
def main():
    perhaps = "perhaps.jpg"
    ninja = Crawler
    key = open("access_dev.txt", "r")
    key = key.read(182)

    page_id = str(108586317548997)
    # instance facebook
    graph = facebook.GraphAPI(access_token = key, version = "2.12")
    

    # crawl the website
    crawled = ninja.crawling_website()
    
    put = graph.put_photo(
            parent_object="me",
            connection_name="feed",
            message="Image from prnt.sc",
            image=open(crawled, "rb"),
            album_path=page_id + "/photos"
        )
    post_id = put['post_id']
    graph.put_comment(object_id=post_id, message='haha my bot sucks')
    graph.put_like(object_id=post_id)
    
    
if __name__ == "__main__":
    main()