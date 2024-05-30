#!/usr/bin/python3
"""
Module to fetch posts from a JSON placeholder
"""
import requests
import csv


def fetch_and_print_posts():
    """
    Fetch posts from json placeholders and print whatever titles
    they have.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(f"Title: {post['title']}")
    else:
        print("Could not fetch posts.")


def fetch_and_save_posts():
    """
    Fetches posts from a json placeholder and saves them
    into a csv file
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()
        posts_data = [{"id": post["id"], "title": post["title"],
                       "body": post["body"]} for post in posts]

        with open('posts.csv', 'w', newline='') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(posts_data)
    else:
        print("Could not fetch posts")
