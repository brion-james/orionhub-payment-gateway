const crypto = require("crypto");

function createTransaction(amount, currency) {
    return {
        id: crypto.randomUUID(),
        amount,
        currency,
        status: "pending"
    };
}

module.exports = {
    createTransaction
};
// Maintenance revision 6
// Maintenance revision 12
