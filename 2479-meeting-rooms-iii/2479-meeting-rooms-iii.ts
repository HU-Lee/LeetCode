function mostBooked(n: number, meetings: number[][]): number {
    const times = new Array<number>(n).fill(0);
    const counts = new Array<number>(n).fill(0);

    meetings.sort((a,b) => a[0] - b[0])

    for (const meeting of meetings) {
        const start = meeting[0]
        const startTimes = times.map((t) => start >= t ? start : t)
        const minTime = Math.min(...startTimes);
        const minRoom = startTimes.indexOf(minTime)
        times[minRoom] = minTime + meeting[1] - start
        counts[minRoom] += 1 
    }
    const maxCounts = Math.max(...counts);
    return counts.indexOf(maxCounts);
};