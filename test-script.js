// Test Script - Sipariş Kalıcılığı Kontrolü
console.log('🚀 Test başlıyor...');

// 1. LocalStorage temizleme
function clearLocalStorage() {
    localStorage.removeItem('allOrders');
    console.log('🧹 LocalStorage temizlendi');
}

// 2. Test siparişi ekleme
function addTestOrder() {
    const testOrder = {
        id: Date.now().toString(),
        userId: "test-user-id",
        userEmail: "info@canerkarakus.com.tr",
        userName: "Test Kullanıcı",
        items: [
            {
                id: 1,
                name: "Test Ürün",
                price: 99.99,
                image: "/test-image.jpg",
                quantity: 1
            }
        ],
        totalAmount: 99.99,
        status: "pending",
        address: {
            title: "Test Adres",
            firstName: "Test",
            lastName: "Kullanıcı",
            phone: "5551234567",
            cityName: "İstanbul",
            districtName: "Kadıköy",
            neighborhood: "Test Mahalle",
            street: "Test Sokak",
            buildingNo: "1"
        },
        paymentMethod: "credit-card",
        createdAt: new Date().toISOString(),
        updatedAt: new Date().toISOString(),
        isNew: true
    };

    const existingOrders = JSON.parse(localStorage.getItem('allOrders') || '[]');
    const updatedOrders = [testOrder, ...existingOrders];
    localStorage.setItem('allOrders', JSON.stringify(updatedOrders));
    console.log('✅ Test siparişi eklendi:', testOrder.id);
    return testOrder.id;
}

// 3. Sipariş kontrolü
function checkOrders() {
    const ordersData = localStorage.getItem('allOrders');
    if (!ordersData) {
        console.log('❌ Sipariş bulunamadı');
        return [];
    }
    
    const orders = JSON.parse(ordersData);
    console.log(`📦 ${orders.length} sipariş bulundu`);
    orders.forEach((order, index) => {
        console.log(`   ${index + 1}. ${order.id} - ${order.userEmail} - ${order.status}`);
    });
    return orders;
}

// Test fonksiyonları
window.testFunctions = {
    clearLocalStorage,
    addTestOrder,
    checkOrders
};

console.log('✅ Test fonksiyonları hazır. Kullanım:');
console.log('- testFunctions.clearLocalStorage()');
console.log('- testFunctions.addTestOrder()');
console.log('- testFunctions.checkOrders()'); 