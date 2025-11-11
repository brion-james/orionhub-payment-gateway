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
// Maintenance revision 18
// Maintenance revision 24
// Maintenance revision 30
// Maintenance revision 36
// Maintenance revision 42
