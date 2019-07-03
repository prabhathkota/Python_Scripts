"""
You are given a valid XML document, and you have to print its score.
The score is calculated by the sum of the score of each element.
For any element, the score is equal to the number of attributes it has.

Enter Command + D to exit from STDIN in MacOS

Input:
6
<feed xml:lang='en'>
    <title>HackerRank</title>
    <subtitle lang='en'>Programming challenges</subtitle>
    <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
    <updated>2013-12-25T12:00:00</updated>
</feed>

Output:
5
"""

import xml.etree.ElementTree as etree
import sys


def get_attr_number(node):
    return len(node.attrib) + sum(get_attr_number(child) for child in node)


if __name__ == '__main__':
    n = sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))

    node = tree.getroot()
    print(get_attr_number(node))


