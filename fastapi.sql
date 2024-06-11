CREATE TABLE posts(
	id SERIAL PRIMARY KEY,
	title TEXT NOT NULL,
	content TEXT NOT NULL,
	published BOOLEAN NOT NULL DEFAULT True,
	created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now()
)

INSERT INTO posts(title, content) VALUES ('first post', 'some interesting stuff'), ('second post', 'yadaydayda');

select * from posts;