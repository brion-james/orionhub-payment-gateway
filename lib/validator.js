function validateTransaction(transaction) {
    if (!transaction) return false;
    if (!transaction.amount) return false;
    if (!transaction.currency) return false;

    return true;
}

module.exports = {
    validateTransaction
};
