"""
Main module
"""
from stabilityWriter import stability
from helper import tone_chart, timeline_source_country

if __name__ == "__main__":
    print(stability)
    neg, neu, pos = tone_chart()
    print(neg, neu, pos)
    base = stability["interest"]
    interest = timeline_source_country(base=(base, 0.1))
    print(interest)
