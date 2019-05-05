"""
Main module
"""
from stabilityWriter import stability
from helper import tone_chart, timeline_source_country, negative_news_count

themes = ['War', 'terrorism']


def negative_news_count_output():
    """
    Nice print of negative_news_count
    :return: None
    """
    output = negative_news_count(topics=themes)
    print('We were able to find this information:')
    for entry in output:
        if output[entry]>0:
            if output[entry]==1:
                print('  === there are', output[entry], 'negative on', entry, 'topic')
            else:
                print('  === there are', output[entry], 'negatives on', entry, 'topic')


if __name__ == "__main__":
    # print(stability)
    neg, neu, pos = tone_chart()
    # print(neg, neu, pos)
    base = stability["interest"]
    interest = timeline_source_country(base=(base, 0.1))
    # print(interest)
    if interest:
        print(
            'Your country seems to be unstable. Would you like to get more information about it? '
            '[Y/n]')
        ans = input(' ==> ')
        if ans in ['Y', 'y', '']:
            print('We are making deeper research. Please stand by...')
            negative_news_count_output()
        else:
            print('As you wish')
    else:
        if abs(stability['mood'][0] - neg) < 0.15:
            print('Your county is stable with rather positive feedback.')
        else:
            print('Your county is stable with rather negative feedback.')
