var Carousel = {
  items: null,
  pane: null,
  
  init: function() {
    this.items = $('.nav-link');
    this.pane = $('.tab-pane');
    this.bindEvents();
  },
  
  bindEvents: function() {
    var self = this;
    
    $('.nexttab').on('click', function() {
      var currentIndex = self.items.filter('.active').index();
      if (currentIndex < self.items.length - 1) {
        self.changeTab(currentIndex, currentIndex + 1);
      }
    });
    
    $('.prevtab').on('click', function() {
      var currentIndex = self.items.filter('.active').index();
      if (currentIndex > 0) {
        self.changeTab(currentIndex, currentIndex - 1);
      }
    });
  },
  
  changeTab: function(currentIndex, nextIndex) {
    this.items.eq(currentIndex).removeClass('active');
    this.items.eq(nextIndex).addClass('active');
    this.pane.eq(currentIndex).removeClass('show active');
    this.pane.eq(nextIndex).addClass('show active');
    location.hash = this.items.eq(nextIndex).attr("href");
  }
};

Carousel.init();