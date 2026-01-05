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
// Maintenance revision 48
// Maintenance revision 54
// Maintenance revision 60
// Maintenance revision 66
// Maintenance revision 72
// Maintenance revision 78
// Maintenance revision 84
// Maintenance revision 90
// Maintenance revision 96
// Maintenance revision 102
// Maintenance revision 108
// Maintenance revision 114
// Maintenance revision 120
