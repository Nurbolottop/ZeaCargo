/* ========================================
   ZeaCargo — Main JavaScript Utilities
   ======================================== */

'use strict';

// =====================
// MOCK DATA
// =====================

const ZeaData = {
  // Current user (simulated)
  currentUser: {
    id: 1,
    name: 'Алексей Иванов',
    role: 'admin', // superadmin | admin | operator | logist | finance | client
    cargo: 'RusCargo KZ',
    avatar: 'АИ',
    email: 'admin@ruscargo.kz'
  },

  // Cargo companies
  companies: [
    { id: 1, name: 'RusCargo KZ',    code: 'RU-001', logo: '🚚', clients: 248, orders: 1842, debt: 892000, status: 'active',  tariff: 'Бизнес',   plan: 'business',   created: '2024-03-15', city: 'Алматы',  since: '2024' },
    { id: 2, name: 'AsiaCargo Pro',  code: 'AS-002', logo: '✈️',  clients: 185, orders: 1103, debt: 340000, status: 'active',  tariff: 'Старт',    plan: 'start',      created: '2024-05-20', city: 'Бишкек',  since: '2024' },
    { id: 3, name: 'SilkRoute Cargo',code: 'SR-003', logo: '📦', clients: 92,  orders: 456,  debt: 120000, status: 'active',  tariff: 'Корпорат', plan: 'corporate',  created: '2024-01-10', city: 'Ташкент', since: '2024' },
    { id: 4, name: 'TuranLogistic',  code: 'TL-004', logo: '🏠', clients: 54,  orders: 210,  debt: 95000,  status: 'paused',  tariff: 'Старт',    plan: 'start',      created: '2024-07-08', city: 'Астана',  since: '2024' },
    { id: 5, name: 'ChinaExpress',   code: 'CE-005', logo: '🐉', clients: 312, orders: 2541, debt: 1200000,status: 'active',  tariff: 'Корпорат', plan: 'corporate',  created: '2023-11-01', city: 'Алматы',  since: '2023' },
  ],

  // Clients
  clients: [
    { id: 1, name: 'Нурбек Асанов', phone: '+996 700 123 456', telegram: '@nurbek_a', orders: 12, debt: 3200, status: 'active', joined: '2024-06-10' },
    { id: 2, name: 'Айгуль Бекова', phone: '+996 555 234 567', telegram: '@aigul_b', orders: 8, debt: 0, status: 'active', joined: '2024-07-22' },
    { id: 3, name: 'Дамир Садыков', phone: '+996 702 345 678', telegram: '@damir_s', orders: 25, debt: 7800, status: 'active', joined: '2024-04-05' },
    { id: 4, name: 'Зарина Омурова', phone: '+996 503 456 789', telegram: '@zarina_o', orders: 3, debt: 1500, status: 'active', joined: '2024-09-11' },
    { id: 5, name: 'Бекзод Рахимов', phone: '+998 90 567 8901', telegram: '@bekzod_r', orders: 18, debt: 0, status: 'inactive', joined: '2024-05-30' },
    { id: 6, name: 'Мадина Карибаева', phone: '+996 770 678 901', telegram: '@madina_k', orders: 7, debt: 4200, status: 'active', joined: '2024-08-14' },
    { id: 7, name: 'Санжар Токтоматов', phone: '+996 999 789 012', telegram: '@sanzhar_t', orders: 31, debt: 12300, status: 'active', joined: '2024-03-20' },
    { id: 8, name: 'Гулнара Юсупова', phone: '+998 94 890 1234', telegram: '@gulnara_y', orders: 5, debt: 0, status: 'active', joined: '2024-10-01' },
  ],

  // Orders
  orders: [
    { id: 1, track: 'CN2024110001', client: 'Нурбек Асанов', shop: 'Taobao', desc: 'Кроссовки Nike', cat: 'Обувь', weight: 1.2, pricePerKg: 800, total: 960, deliveryStatus: 'in_transit', payStatus: 'unpaid', created: '2024-11-01', arrival: '2024-11-20' },
    { id: 2, track: 'CN2024110002', client: 'Айгуль Бекова', shop: '1688.com', desc: 'Платье женское', cat: 'Одежда', weight: 0.5, pricePerKg: 800, total: 400, deliveryStatus: 'ready', payStatus: 'paid', created: '2024-11-02', arrival: '2024-11-18' },
    { id: 3, track: 'CN2024110003', client: 'Дамир Садыков', shop: 'JD.com', desc: 'Ноутбук Lenovo', cat: 'Электроника', weight: 3.0, pricePerKg: 1200, total: 3600, deliveryStatus: 'warehouse', payStatus: 'partial', created: '2024-11-03', arrival: '2024-11-25' },
    { id: 4, track: 'CN2024110004', client: 'Зарина Омурова', shop: 'Pinduoduo', desc: 'Часы женские', cat: 'Аксессуары', weight: 0.3, pricePerKg: 800, total: 240, deliveryStatus: 'sorting', payStatus: 'unpaid', created: '2024-11-04', arrival: '2024-11-22' },
    { id: 5, track: 'CN2024110005', client: 'Санжар Токтоматов', shop: 'Alibaba', desc: 'Запчасти авто', cat: 'Автотовары', weight: 8.5, pricePerKg: 700, total: 5950, deliveryStatus: 'arrived', payStatus: 'unpaid', created: '2024-10-28', arrival: '2024-11-15' },
    { id: 6, track: 'CN2024110006', client: 'Мадина Карибаева', shop: 'Taobao', desc: 'Косметика набор', cat: 'Косметика', weight: 1.8, pricePerKg: 800, total: 1440, deliveryStatus: 'issued', payStatus: 'paid', created: '2024-10-25', arrival: '2024-11-10' },
    { id: 7, track: 'CN2024110007', client: 'Нурбек Асанов', shop: '1688.com', desc: 'Куртка зимняя', cat: 'Одежда', weight: 2.1, pricePerKg: 800, total: 1680, deliveryStatus: 'ready', payStatus: 'unpaid', created: '2024-11-05', arrival: '2024-11-19' },
    { id: 8, track: 'CN2024110008', client: 'Бекзод Рахимов', shop: 'JD.com', desc: 'Игрушки детские', cat: 'Детские товары', weight: 4.2, pricePerKg: 800, total: 3360, deliveryStatus: 'prepared', payStatus: 'paid', created: '2024-11-06', arrival: '2024-11-24' },
  ],

  // Products (catalog)
  products: [
    { id: 1, name: 'Кроссовки Nike Air Max',    category: 'Обувь',        price: 4500,  priceCny: 280, shop: 'Taobao',    status: 'active', requests: 12, delivery: '15-20 дней', img: '👟' },
    { id: 2, name: 'Куртка Puffer женская',       category: 'Одежда',       price: 3200,  priceCny: 195, shop: '1688.com',  status: 'active', requests: 8,  delivery: '15-20 дней', img: '🧥' },
    { id: 3, name: 'Apple AirPods Pro 2',         category: 'Электроника',  price: 18000, priceCny: 900, shop: 'JD.com',    status: 'active', requests: 24, delivery: '10-15 дней', img: '🎧' },
    { id: 4, name: 'Сумка женская кожаная',       category: 'Аксессуары',   price: 5500,  priceCny: 340, shop: 'Pinduoduo', status: 'active', requests: 5,  delivery: '20-25 дней', img: '👜' },
    { id: 5, name: 'Увлажнитель воздуха',         category: 'Для дома',     price: 2100,  priceCny: 130, shop: 'Taobao',    status: 'active', requests: 3,  delivery: '15-20 дней', img: '💧' },
    { id: 6, name: 'Крем для лица LANEIGE',       category: 'Косметика',    price: 3800,  priceCny: 238, shop: '1688.com',  status: 'hidden', requests: 6,  delivery: '15-20 дней', img: '🧴' },
    { id: 7, name: 'Конструктор LEGO City',       category: 'Детские',      price: 4200,  priceCny: 260, shop: 'JD.com',    status: 'active', requests: 9,  delivery: '15-20 дней', img: '🧸' },
    { id: 8, name: 'Зимние ботинки UGG',          category: 'Обувь',        price: 7500,  priceCny: 460, shop: 'Taobao',    status: 'active', requests: 18, delivery: '20-25 дней', img: '🥾' },
    { id: 9, name: 'Смарт-часы Samsung',          category: 'Электроника',  price: 12000, priceCny: 750, shop: 'JD.com',    status: 'active', requests: 7,  delivery: '10-15 дней', img: '⌚' },
    { id:10, name: 'Платье базовое',              category: 'Одежда',       price: 1800,  priceCny: 112, shop: 'Pinduoduo', status: 'active', requests: 14, delivery: '15-20 дней', img: '👗' },
  ],

  // Purchase Requests (выкуп)
  purchaseRequests: [
    { id: 1, client: 'Нурбек Асанов',   product: 'Adidas Ultraboost',    link: 'https://taobao.com/item/1', qty: 1, size: '43',  color: 'Серый',    budget: 8500,  status: 'new',       date: '2024-11-06', comment: 'Оригинал желателен' },
    { id: 2, client: 'Зарина Омурова',  product: 'Платье летнее',        link: 'https://1688.com/item/2',  qty: 2, size: 'M',    color: 'Розовый',  budget: 3200,  status: 'new',       date: '2024-11-05', comment: '' },
    { id: 3, client: 'Дамир Садыков',   product: 'Наушники Baseus TWS', link: 'https://jd.com/item/3',    qty: 1, size: '',     color: 'Чёрный',   budget: 4200,  status: 'inwork',    date: '2024-11-04', comment: 'Нужна гарантия' },
    { id: 4, client: 'Мадина Карибаева',product: 'Тональный крем',       link: 'https://taobao.com/item/4',qty: 3, size: '',     color: '#32W',     budget: 2100,  status: 'new',       date: '2024-11-03', comment: '' },
    { id: 5, client: 'Санжар Токтоматов',product:'Масло моторное 5W40',  link: 'https://alibaba.com/item/5',qty:4, size: '',    color: '',         budget: 12000, status: 'inwork',    date: '2024-11-01', comment: 'Брендовое только' },
    { id: 6, client: 'Айгуль Бекова',   product: 'Зимние перчатки',     link: 'https://taobao.com/item/6',qty: 1, size: 'L',    color: 'Бежевый',  budget: 1200,  status: 'new',       date: '2024-11-06', comment: '' },
    { id: 7, client: 'Бекзод Рахимов',  product: 'Рюкзак школьный',     link: 'https://1688.com/item/7',  qty: 2, size: '',     color: 'Синий',    budget: 5600,  status: 'done',      date: '2024-10-28', comment: '' },
    { id: 8, client: 'Гулнара Юсупова', product: 'Детская игрушка',      link: 'https://jd.com/item/8',    qty: 1, size: '',     color: '',         budget: 3000,  status: 'new',       date: '2024-11-07', comment: 'Возраст 3-5 лет' },
  ],

  // Requests (buyout)
  requests: [
    { id: 1, client: 'Нурбек Асанов', product: 'Air Max 270', link: 'taobao.com/...', qty: 1, size: '43', color: 'Белый', status: 'confirmed', date: '2024-11-05' },
    { id: 2, client: 'Зарина Омурова', product: 'Платье летнее', link: '1688.com/...', qty: 2, size: 'M', color: 'Розовый', status: 'new', date: '2024-11-06' },
    { id: 3, client: 'Дамир Садыков', product: 'Наушники Baseus', link: 'jd.com/...', qty: 1, size: '-', color: 'Чёрный', status: 'purchased', date: '2024-11-04' },
    { id: 4, client: 'Мадина Карибаева', product: 'Тональный крем', link: 'taobao.com/...', qty: 3, size: '-', color: '#32W', status: 'rejected', date: '2024-11-03' },
    { id: 5, client: 'Санжар Токтоматов', product: 'Масло моторное 5W40', link: 'alibaba.com/...', qty: 4, size: '-', color: '-', status: 'in_delivery', date: '2024-11-01' },
  ],

  // Payments
  payments: [
    { id: 1, client: 'Айгуль Бекова', order: 'CN2024110002', amount: 400, method: 'cash', date: '2024-11-12', operator: 'Алексей Иванов' },
    { id: 2, client: 'Мадина Карибаева', order: 'CN2024110006', amount: 1440, method: 'card', date: '2024-11-11', operator: 'Алексей Иванов' },
    { id: 3, client: 'Бекзод Рахимов', order: 'CN2024110008', amount: 3360, method: 'transfer', date: '2024-11-10', operator: 'Алексей Иванов' },
    { id: 4, client: 'Нурбек Асанов', order: 'CN2024110001', amount: 500, method: 'cash', date: '2024-11-08', operator: 'Алексей Иванов' },
  ],

  // Delivery statuses
  deliveryStatuses: {
    warehouse_expected: { label: 'Ожидается на складе', color: 'neutral', icon: '⏳' },
    warehouse:          { label: 'Принят на складе',    color: 'info',    icon: '📥' },
    prepared:           { label: 'Подготовлен к отправке', color: 'purple', icon: '📦' },
    in_transit:         { label: 'В пути',              color: 'warning', icon: '🚚' },
    arrived:            { label: 'Прибыл в страну',     color: 'teal',    icon: '✈️' },
    sorting:            { label: 'На сортировке',       color: 'orange',  icon: '🔄' },
    ready:              { label: 'Готов к выдаче',      color: 'success', icon: '✅' },
    issued:             { label: 'Выдан клиенту',       color: 'success', icon: '🎁' },
    problem:            { label: 'Проблема / Возврат',  color: 'danger',  icon: '⚠️' },
  },

  // Payment statuses
  payStatuses: {
    unpaid:  { label: 'Не оплачен',         color: 'danger'  },
    partial: { label: 'Частично оплачен',   color: 'warning' },
    paid:    { label: 'Полностью оплачен',  color: 'success' },
  },

  // Request statuses
  requestStatuses: {
    new:        { label: 'Новая',                    color: 'info'    },
    review:     { label: 'На рассмотрении',          color: 'neutral' },
    pending:    { label: 'Ожидает подтверждения',    color: 'warning' },
    confirmed:  { label: 'Подтверждена',             color: 'success' },
    rejected:   { label: 'Отклонена',               color: 'danger'  },
    purchased:  { label: 'Выкуплена',               color: 'purple'  },
    in_delivery:{ label: 'Передана в доставку',      color: 'teal'    },
  },

  // Warehouses
  warehouses: [
    { id: 1, city: 'Guangzhou', address: 'Guangdong Province, Guangzhou, Baiyun District, No.123', recipient: 'RusCargo GZ', phone: '+86 138 0013 8000', code: 'GZ001' },
    { id: 2, city: 'Yiwu', address: 'Zhejiang Province, Yiwu, Chouzhou North Road, No.88', recipient: 'RusCargo YW', phone: '+86 139 8900 1234', code: 'YW001' },
  ],
};

// =====================
// UTILITIES
// =====================

const ZeaUtils = {
  // Format currency
  formatMoney(amount, currency = 'сом') {
    return `${Number(amount).toLocaleString('ru-RU')} ${currency}`;
  },

  // Format date
  formatDate(dateStr, format = 'short') {
    const d = new Date(dateStr);
    const opts = format === 'short'
      ? { day: '2-digit', month: '2-digit', year: 'numeric' }
      : { day: 'long', month: 'long', year: 'numeric' };
    return d.toLocaleDateString('ru-RU', opts);
  },

  // Generate initials from name
  getInitials(name) {
    return name.split(' ').slice(0, 2).map(w => w[0]).join('').toUpperCase();
  },

  // Generate avatar color from string
  getAvatarColor(str) {
    const colors = [
      'linear-gradient(135deg, #6C63FF, #5248CC)',
      'linear-gradient(135deg, #10B981, #059669)',
      'linear-gradient(135deg, #F59E0B, #D97706)',
      'linear-gradient(135deg, #EF4444, #C53030)',
      'linear-gradient(135deg, #3B82F6, #2563EB)',
      'linear-gradient(135deg, #8B5CF6, #7C3AED)',
      'linear-gradient(135deg, #EC4899, #DB2777)',
      'linear-gradient(135deg, #14B8A6, #0D9488)',
    ];
    let hash = 0;
    for (let c of str) hash = hash * 31 + c.charCodeAt(0);
    return colors[Math.abs(hash) % colors.length];
  },

  // Create badge HTML
  createBadge(type, label) {
    return `<span class="badge badge-${type}">${label}</span>`;
  },

  // Create avatar HTML
  createAvatar(name, size = 'md') {
    const initials = ZeaUtils.getInitials(name);
    const color = ZeaUtils.getAvatarColor(name);
    return `<div class="avatar avatar-${size}" style="background: ${color};">${initials}</div>`;
  },

  // Pluralize RU
  pluralize(n, forms) {
    const mod10 = n % 10, mod100 = n % 100;
    if (mod10 === 1 && mod100 !== 11) return forms[0];
    if ([2,3,4].includes(mod10) && ![12,13,14].includes(mod100)) return forms[1];
    return forms[2];
  },

  // Debounce
  debounce(fn, delay = 300) {
    let timer;
    return (...args) => {
      clearTimeout(timer);
      timer = setTimeout(() => fn(...args), delay);
    };
  },

  // Get URL param
  getParam(key) {
    return new URLSearchParams(window.location.search).get(key);
  },

  // Relative filepath helper
  getRelativePath() {
    const depth = location.pathname.split('/').filter(Boolean).length;
    return depth <= 1 ? './' : '../'.repeat(depth - 1);
  }
};

// =====================
// SIDEBAR MANAGER
// =====================
const Sidebar = {
  el: null,
  topbar: null,
  isCollapsed: false,
  overlay: null,

  init() {
    this.el = document.querySelector('.sidebar');
    this.topbar = document.querySelector('.topbar');
    if (!this.el) return;

    // Forces sidebar to always be open on desktop
    this.isCollapsed = false;
    this.expand();
    localStorage.removeItem('sidebar_collapsed');

    // Create mobile overlay
    this.overlay = document.createElement('div');
    this.overlay.style.cssText = 'display:none;position:fixed;inset:0;background:rgba(0,0,0,0.5);z-index:99;backdrop-filter:blur(2px);';
    this.overlay.addEventListener('click', () => this.hideMobile());
    document.body.appendChild(this.overlay);

    // Toggle button
    const toggleBtn = document.querySelector('[data-sidebar-toggle]');
    if (toggleBtn) {
      toggleBtn.addEventListener('click', () => {
        if (window.innerWidth <= 1024) {
          // Mobile: toggle show class
          const isShown = this.el.classList.contains('show');
          isShown ? this.hideMobile() : this.showMobile();
        } else {
          // Desktop: collapse/expand
          this.toggle();
        }
      });
    }

    // Active link
    this.setActiveLink();

    // On resize, reset mobile state
    window.addEventListener('resize', () => {
      if (window.innerWidth > 1024) {
        this.hideMobile();
        if (!this.isCollapsed) this.expand();
      }
    });
  },

  showMobile() {
    this.el.classList.add('show');
    this.overlay.style.display = 'block';
    document.body.style.overflow = 'hidden';
  },

  hideMobile() {
    this.el.classList.remove('show');
    this.overlay.style.display = 'none';
    document.body.style.overflow = '';
  },

  toggle() {
    this.isCollapsed ? this.expand() : this.collapse();
  },

  collapse(animate = true) {
    this.isCollapsed = true;
    this.el.classList.add('collapsed');
    this.topbar?.classList.add('sidebar-collapsed');
    document.querySelector('.main-content')?.classList.add('sidebar-collapsed');
    localStorage.setItem('sidebar_collapsed', 'true');
  },

  expand() {
    this.isCollapsed = false;
    this.el.classList.remove('collapsed');
    this.topbar?.classList.remove('sidebar-collapsed');
    document.querySelector('.main-content')?.classList.remove('sidebar-collapsed');
    localStorage.setItem('sidebar_collapsed', 'false');
  },

  setActiveLink() {
    const currentPath = location.pathname;
    document.querySelectorAll('.sidebar-link').forEach(link => {
      const href = link.getAttribute('href');
      if (href && href !== '/' && currentPath.startsWith(href)) {
        link.classList.add('active');
      }
    });
  }
};


// =====================
// TOAST MANAGER
// =====================
const Toast = {
  container: null,

  init() {
    this.container = document.querySelector('.toast-container');
    if (!this.container) {
      this.container = document.createElement('div');
      this.container.className = 'toast-container';
      document.body.appendChild(this.container);
    }
  },

  show(type = 'info', title, message = '', duration = 4000) {
    if (!this.container) this.init();

    const icons = { success: '✅', error: '❌', warning: '⚠️', info: 'ℹ️' };

    const toast = document.createElement('div');
    toast.className = `toast ${type}`;
    toast.innerHTML = `
      <span class="toast-icon">${icons[type] || icons.info}</span>
      <div class="toast-content">
        <div class="toast-title">${title}</div>
        ${message ? `<div class="toast-msg">${message}</div>` : ''}
      </div>
      <span class="toast-close" onclick="this.parentElement.remove()">✕</span>
    `;

    this.container.appendChild(toast);
    requestAnimationFrame(() => {
      requestAnimationFrame(() => toast.classList.add('show'));
    });

    setTimeout(() => {
      toast.classList.remove('show');
      setTimeout(() => toast.remove(), 400);
    }, duration);

    return toast;
  },

  success(title, msg) { return this.show('success', title, msg); },
  error(title, msg)   { return this.show('error',   title, msg); },
  warning(title, msg) { return this.show('warning', title, msg); },
  info(title, msg)    { return this.show('info',    title, msg); },
};

// =====================
// MODAL MANAGER
// =====================
const Modal = {
  open(id) {
    const overlay = document.getElementById(id);
    if (!overlay) return;
    overlay.classList.add('active');
    document.body.style.overflow = 'hidden';
    overlay.addEventListener('click', (e) => {
      if (e.target === overlay) Modal.close(id);
    }, { once: true });
  },

  close(id) {
    const overlay = document.getElementById(id);
    if (!overlay) return;
    overlay.classList.remove('active');
    document.body.style.overflow = '';
  },

  closeAll() {
    document.querySelectorAll('.modal-overlay.active').forEach(m => {
      m.classList.remove('active');
    });
    document.body.style.overflow = '';
  }
};

// =====================
// TABS MANAGER
// =====================
const Tabs = {
  init(container = document) {
    container.querySelectorAll('[data-tab]').forEach(btn => {
      btn.addEventListener('click', () => {
        const target = btn.dataset.tab;
        const group = btn.dataset.tabGroup || 'default';

        // Deactivate all in group
        container.querySelectorAll(`[data-tab-group="${group}"], [data-tab]:not([data-tab-group])`).forEach(b => b.classList.remove('active'));
        container.querySelectorAll(`[data-tab-content-group="${group}"], [data-tab-content]`).forEach(c => c.classList.remove('active'));

        // Activate target
        btn.classList.add('active');
        const content = container.querySelector(`[data-tab-content="${target}"]`);
        if (content) content.classList.add('active');
      });
    });

    // Activate first tab in each group
    const activated = new Set();
    container.querySelectorAll('[data-tab]').forEach(btn => {
      const group = btn.dataset.tabGroup || 'default';
      if (!activated.has(group)) {
        btn.click();
        activated.add(group);
      }
    });
  }
};

// =====================
// ACCORDION
// =====================
const Accordion = {
  init(container = document) {
    container.querySelectorAll('.accordion-header').forEach(header => {
      header.addEventListener('click', () => {
        const item = header.closest('.accordion-item');
        const isOpen = item.classList.contains('open');

        // Close all (optional: single-open mode)
        // container.querySelectorAll('.accordion-item.open').forEach(i => i.classList.remove('open'));

        item.classList.toggle('open', !isOpen);
      });
    });
  }
};

// =====================
// DROPDOWN
// =====================
const Dropdown = {
  init() {
    document.addEventListener('click', (e) => {
      const trigger = e.target.closest('[data-dropdown]');
      if (trigger) {
        const menuId = trigger.dataset.dropdown;
        const menu = document.getElementById(menuId);
        if (menu) {
          const isActive = menu.classList.contains('active');
          // Close all
          document.querySelectorAll('.dropdown-menu.active').forEach(m => m.classList.remove('active'));
          if (!isActive) menu.classList.add('active');
        }
        return;
      }
      // Close if clicked outside
      if (!e.target.closest('.dropdown-menu')) {
        document.querySelectorAll('.dropdown-menu.active').forEach(m => m.classList.remove('active'));
      }
    });
  }
};

// =====================
// TOGGLE SWITCH
// =====================
function initToggles(container = document) {
  container.querySelectorAll('.toggle').forEach(toggle => {
    toggle.addEventListener('click', () => {
      toggle.classList.toggle('active');
    });
  });
}

// =====================
// FILE UPLOAD
// =====================
function initFileUploads(container = document) {
  container.querySelectorAll('.file-upload').forEach(zone => {
    const input = zone.querySelector('input[type="file"]');

    zone.addEventListener('dragover', (e) => {
      e.preventDefault();
      zone.classList.add('dragover');
    });
    zone.addEventListener('dragleave', () => zone.classList.remove('dragover'));
    zone.addEventListener('drop', (e) => {
      e.preventDefault();
      zone.classList.remove('dragover');
      if (input) { input.files = e.dataTransfer.files; input.dispatchEvent(new Event('change')); }
    });
    zone.addEventListener('click', () => input?.click());
  });
}

// =====================
// SEARCH FILTER (client-side)
// =====================
function initSearch(inputSel, targetSel, attrs = ['data-search']) {
  const input = document.querySelector(inputSel);
  if (!input) return;

  const debouncedFilter = ZeaUtils.debounce(() => {
    const query = input.value.toLowerCase().trim();
    document.querySelectorAll(targetSel).forEach(item => {
      const text = attrs.map(a => (item.getAttribute(a) || item.textContent || '').toLowerCase()).join(' ');
      item.style.display = text.includes(query) ? '' : 'none';
    });
  }, 200);

  input.addEventListener('input', debouncedFilter);
}

// =====================
// COUNTER ANIMATION
// =====================
function animateCounter(el, target, duration = 1200) {
  const start = 0;
  const step = target / (duration / 16);
  let current = start;

  const timer = setInterval(() => {
    current = Math.min(current + step, target);
    el.textContent = Math.round(current).toLocaleString('ru-RU');
    if (current >= target) clearInterval(timer);
  }, 16);
}

function initCounters() {
  document.querySelectorAll('[data-counter]').forEach(el => {
    const target = parseInt(el.dataset.counter);
    if (!isNaN(target)) animateCounter(el, target, 1000);
  });
}

// =====================
// CHARTS HELPER (Chart.js)
// =====================
const ZeaCharts = {
  defaults: {
    color: '#94A3B8',
    gridColor: 'rgba(255,255,255,0.05)',
    fontFamily: 'Inter, sans-serif',
  },

  getDefaults() {
    return {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: {
          labels: { color: this.defaults.color, font: { family: this.defaults.fontFamily, size: 12 } }
        },
        tooltip: {
          backgroundColor: '#1A1A35',
          borderColor: 'rgba(255,255,255,0.1)',
          borderWidth: 1,
          titleColor: '#F1F5F9',
          bodyColor: '#94A3B8',
          padding: 12,
          cornerRadius: 10,
        }
      },
      scales: {
        x: {
          ticks: { color: this.defaults.color, font: { family: this.defaults.fontFamily, size: 11 } },
          grid: { color: this.defaults.gridColor }
        },
        y: {
          ticks: { color: this.defaults.color, font: { family: this.defaults.fontFamily, size: 11 } },
          grid:  { color: this.defaults.gridColor }
        }
      }
    };
  },

  createLine(canvasId, labels, datasets, opts = {}) {
    const ctx = document.getElementById(canvasId);
    if (!ctx) return null;
    return new Chart(ctx, {
      type: 'line',
      data: { labels, datasets: datasets.map(d => ({
        tension: 0.4,
        borderWidth: 2,
        pointRadius: 4,
        pointHoverRadius: 6,
        fill: true,
        ...d
      }))},
      options: { ...this.getDefaults(), ...opts }
    });
  },

  createBar(canvasId, labels, datasets, opts = {}) {
    const ctx = document.getElementById(canvasId);
    if (!ctx) return null;
    return new Chart(ctx, {
      type: 'bar',
      data: { labels, datasets: datasets.map(d => ({
        borderRadius: 6,
        borderSkipped: false,
        ...d
      }))},
      options: { ...this.getDefaults(), ...opts }
    });
  },

  createDonut(canvasId, labels, data, colors, opts = {}) {
    const ctx = document.getElementById(canvasId);
    if (!ctx) return null;
    return new Chart(ctx, {
      type: 'doughnut',
      data: {
        labels,
        datasets: [{ data, backgroundColor: colors, borderWidth: 0, borderRadius: 4, hoverOffset: 8 }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        cutout: '72%',
        plugins: {
          legend: {
            position: 'bottom',
            labels: { color: '#94A3B8', padding: 16, font: { family: 'Inter, sans-serif', size: 12 }, boxWidth: 12, boxHeight: 12 }
          },
          tooltip: this.getDefaults().plugins.tooltip
        }
      }
    });
  }
};

// =====================
// INIT ALL
// =====================
document.addEventListener('DOMContentLoaded', () => {
  Sidebar.init();
  Toast.init();
  Tabs.init();
  Accordion.init();
  Dropdown.init();
  initToggles();
  initFileUploads();
  initCounters();

  // Close modal on ESC
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') Modal.closeAll();
  });

  // Modal close buttons
  document.querySelectorAll('[data-modal-close]').forEach(btn => {
    btn.addEventListener('click', () => {
      const modal = btn.closest('.modal-overlay');
      if (modal) Modal.close(modal.id);
    });
  });

  // Modal open buttons
  document.querySelectorAll('[data-modal-open]').forEach(btn => {
    btn.addEventListener('click', () => {
      Modal.open(btn.dataset.modalOpen);
    });
  });

  // Page entry animation
  document.querySelectorAll('.page-content, .client-page').forEach(el => {
    el.classList.add('animate-fade-up');
  });
});
