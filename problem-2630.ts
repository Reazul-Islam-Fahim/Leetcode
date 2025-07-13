type Fn = (...params: any[]) => any

function memoize(fn: Fn): Fn {
    const cache = new Map();

    return function (...args: any[]) {
        let current = cache;

        for (const arg of args) {
            if (!current.has(arg)) {
                current.set(arg, new Map());
            }
            current = current.get(arg);
        }

        if (!current.has('result')) {
            current.set('result', fn(...args));
        }

        return current.get('result');
    };
}
