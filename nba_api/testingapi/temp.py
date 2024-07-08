import sys

sys.path.append('..')

if __name__ == '__main__':


    with open('../logs/fv.log', 'r') as f:
        lines = f.readlines()
        filtered = filter(lambda x: 'Feature vector calculation for game' in x, lines)

        tot_time = 0
        processed = 0
        for line in filtered:
            tot_time += float(line.split(' ')[-2])
            processed += 1

                       # tot completed teams
        expected_end = ((1320 - 28) * tot_time/processed) / 3600

        print(f'Completed {processed} fvs in avg time {tot_time/processed}, expected end for this season in {expected_end} hours')
