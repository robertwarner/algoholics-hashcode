import os

from input_parser import VideoServiceNetwork


def solve(network):
    solution = [ set() for _ in range(network.num_caches) ]
    request_satisfied = [ False ] * network.num_requests
    cache_sizes = [ network.cache_size ] * network.num_caches

    for _, cache_id, video_id, request_id in sorted(network.greedy_list, reverse=True):
        video_size = network.video_size_list[video_id]
        if not request_satisfied[request_id] \
                and video_id not in solution[cache_id] \
                and video_size <= cache_sizes[cache_id]:
            cache_sizes[cache_id] -= video_size
            solution[cache_id].add(video_id)
            request_satisfied[request_id] = True

    return solution


def write_output(solution, file):
    with open(file, 'w') as f:
        f.write(str(sum(len(cached_videos) > 0 for cached_videos in solution)) + '\n')
        for cache_id, cached_videos in enumerate(solution):
            if len(cached_videos) > 0:
                f.write(str(cache_id))
                for video_id in cached_videos:
                    f.write(' ' + str(video_id))
                f.write('\n')


if __name__ == '__main__':
    for f in os.listdir('./data/'):
        if f.endswith('.in'):
            solution = solve(VideoServiceNetwork('./data/' + f))
            write_output(solution, './data/' + f.replace('.in', '.out'))
