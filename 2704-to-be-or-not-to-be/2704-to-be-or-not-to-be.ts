type ToBeOrNotToBe = {
    toBe: (val: any) => boolean;
    notToBe: (val: any) => boolean;
};

function expect(val: any): ToBeOrNotToBe {
    const expected = val;
    return {
        toBe: (target: any) => {
            if (target === expected) return true
            else throw new Error("Not Equal")
        },
        notToBe: (target: any) => {
            if (target !== expected) return true
            else throw new Error("Equal")
        }
    }
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */