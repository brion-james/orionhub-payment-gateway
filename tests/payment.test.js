const assert = require("assert");

function validateAmount(amount) {
    return Number.isFinite(amount) && amount > 0;
}

assert.strictEqual(validateAmount(100), true);
assert.strictEqual(validateAmount(-1), false);
