#! /usr/bin/env python
# -*- coding: utf-8 -*-


"""
无向有权图找最短路径。
"""

from collections import deque


def line_input():
    return [int(each) for each in raw_input().split(' ')]


cities_total, roads_total, city_start_id, city_end_id = line_input()

cities_team_amount = line_input()
roads = []
for i in xrange(roads_total):
    road = line_input()
    roads.append(road)

adjacent_matrix = [[-1]*cities_total for row in xrange(cities_total)]   # dis
for i in xrange(cities_total):
    adjacent_matrix[i][i] = 0  # self-2-self distance is zero
route_matrix = [[-1]*cities_total for row in xrange(cities_total)]
shortest_dis = -1

for road in roads:
    adjacent_matrix[road[0]][road[1]] =\
        adjacent_matrix[road[1]][road[0]] = road[2]


# breadth-first-search
# (distance, last_city)
visited_cities = deque()


def bfs(current_city_id):
    global shortest_dis, visited_cities
    for city_id, dis in enumerate(adjacent_matrix[current_city_id]):
        if dis <= 0:
            continue
        if route_matrix[city_start_id][current_city_id] == city_id:
            continue

        tmp_dis = dis + adjacent_matrix[city_start_id][current_city_id]

        if adjacent_matrix[city_start_id][city_id] < 0:
            adjacent_matrix[city_start_id][city_id] = tmp_dis
            route_matrix[city_start_id][city_id] = current_city_id
        else:
            origin_route = route_matrix[city_start_id][city_id]
            if tmp_dis < adjacent_matrix[city_start_id][city_id]:
                adjacent_matrix[city_start_id][city_id] = tmp_dis
                route_matrix[city_start_id][city_id] = current_city_id
            elif tmp_dis == adjacent_matrix[city_start_id][city_id]:
                if type(origin_route) == int:
                    if origin_route >= 0:
                        route_matrix[city_start_id][city_id] = [origin_route, current_city_id]
                    else:
                        route_matrix[city_start_id][city_id] = current_city_id
                elif type(origin_route) == list:
                    route_matrix[city_start_id][city_id].append(current_city_id)

        if city_id == city_end_id:
            pass
        else:
            visited_cities.append(city_id)

bfs(city_start_id)
while len(visited_cities) > 0:
    city_id = visited_cities.popleft()
    bfs(city_id)

shortest_distance = adjacent_matrix[city_start_id][city_end_id]
routes = route_matrix[city_start_id][city_end_id]


def cal_path(tmp_route):
    path = deque()
    path.appendleft(city_end_id)
    path.appendleft(tmp_route)
    while route_matrix[city_start_id][tmp_route] >= 0:
        tmp_route = route_matrix[city_start_id][tmp_route]
        path.appendleft(tmp_route)
    team_sum_tmp = 0
    for city in path:
        team_sum_tmp += cities_team_amount[city]
    return team_sum_tmp


if type(routes) == int:
    team_sum = cal_path(routes)
    number_route = 1
else:
    number_route = len(routes)
    teams = []
    for route in routes:
        tmp_team_sum = cal_path(route)
        teams.append(tmp_team_sum)
    teams = sorted(teams, reverse=True)
    team_sum = teams[0]

print number_route, team_sum
