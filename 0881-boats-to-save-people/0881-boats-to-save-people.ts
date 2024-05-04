function numRescueBoats(people: number[], limit: number): number {
    people.sort((a,b) => a-b)

    let left = 0
    let right = people.length - 1
    let count = 0
    while (left < right) {
        const boat = people[left] + people[right]
        if (boat <= limit) {
            left++
            right--
        } else {
            right--
        }
        count++
    }
    if (left == right) {
        count++
    }
    return count
};