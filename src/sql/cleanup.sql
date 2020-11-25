-- clean up old posts from the database
DELETE FROM posts
WHERE strftime("%s", "now")-date_added > 259200; -- 3 days