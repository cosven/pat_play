#! /usr/bin/env python
# -*- coding: utf-8 -*-


"""
无向有权图找最短路径。

代码比想象的多，比较丑。

感知递归的特征.

注意点：
1. if ... else 判断不要漏
2. start 和　end 的city可以是一样的
3. 递归的变量。。。感悟
"""
import sys
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

if city_start_id == city_end_id:
    print 1, cities_team_amount[city_start_id]
    sys.exit(0)

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

        append_flag = True
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
                    if origin_route >= 0 and origin_route != current_city_id:
                        route_matrix[city_start_id][city_id] =\
                                [origin_route, current_city_id]
                    else:
                        route_matrix[city_start_id][city_id] = current_city_id
                else:   # list
                    if current_city_id in route_matrix[city_start_id][city_id]:
                        pass
                    else:
                        route_matrix[city_start_id][city_id].append(
                            current_city_id)
            else:
                append_flag = False

        if city_id == city_end_id:
            pass
        else:
            if append_flag:
                visited_cities.append(city_id)


bfs(city_start_id)
while len(visited_cities) > 0:
    # print visited_cities
    city_id = visited_cities.popleft()
    bfs(city_id)

# calculate path

# print
# print

number_route = 0
total_teams = []


def cal_path(current_city, current_teams_num):
    global number_route, total_teams

    current_teams_num += cities_team_amount[current_city]
    # print "c:", current_city,

    neighbours = route_matrix[city_start_id][current_city]
    if type(neighbours) is int:
        neighbours = [neighbours]

    tmp_num = current_teams_num
    for neighbour in neighbours:
        if neighbour == city_start_id:
            # print 'n:', neighbour,
            number_route += 1
            current_teams_num += cities_team_amount[neighbour]
            total_teams.append(current_teams_num)
            # print "end"
        else:
            # print "next loop:", current_teams_num
            cal_path(neighbour, tmp_num)


# print route_matrix
cal_path(city_end_id, 0)
total_teams = sorted(total_teams, reverse=True)
print number_route, total_teams[0]
