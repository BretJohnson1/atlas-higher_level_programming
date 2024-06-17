-- This script lists all of the cities that are in California
SELECT cities.id, cities.name FROM cities, states WHERE cities.state_id = states.id AND states.name = 'California' ORDER BY cities.id ASC;
