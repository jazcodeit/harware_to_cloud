CREATE TABLE sensor_data (
    timestamp DATETIME NOT NULL,
    device_port VARCHAR(255) NOT NULL,
    farthest_distance FLOAT NOT NULL,
    closest_distance FLOAT NOT NULL,
    average_distance FLOAT NOT NULL
);