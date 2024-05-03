function compareVersion(version1: string, version2: string): number {
    const arr1 = version1.split(".").map(Number)
    const arr2 = version2.split(".").map(Number)

    let i = 0
    let j = 0
    while (i<arr1.length || j<arr2.length) {
        if (i >= arr1.length) {
            if (arr2[j]>0) return -1
            j++
            continue
        } else if (j >= arr2.length) {
            if (arr1[i]>0) return 1
            i++
            continue
        } else if (arr1[i] != arr2[j]) {
            return arr1[i] > arr2[j] ? 1 : -1
        }
        j++
        i++
    }
    return 0 
};