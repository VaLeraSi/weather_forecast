CREATE TABLE weather (
  id SERIAL PRIMARY KEY,
  city VARCHAR(255) NOT NULL,
  temperature FLOAT NOT NULL,
  description VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT NOW()
);