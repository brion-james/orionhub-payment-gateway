const assert = require("assert");

function validateAmount(amount) {
    return Number.isFinite(amount) && amount > 0;
}

assert.strictEqual(validateAmount(100), true);
assert.strictEqual(validateAmount(-1), false);
// Test revision 3
// Test revision 9
// Test revision 15
// Test revision 21
// Test revision 27
// Test revision 33
