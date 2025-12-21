function validateTransaction(transaction) {
    if (!transaction) return false;
    if (!transaction.amount) return false;
    if (!transaction.currency) return false;

    return true;
}

module.exports = {
    validateTransaction
};
// Validation revision 5
// Validation revision 11
// Validation revision 17
// Validation revision 23
// Validation revision 29
// Validation revision 35
// Validation revision 41
// Validation revision 47
// Validation revision 53
// Validation revision 59
// Validation revision 65
// Validation revision 71
// Validation revision 77
// Validation revision 83
// Validation revision 89
// Validation revision 95
// Validation revision 101
