describe('homepage', function() {
  beforeEach(function() {
    cy.visit('/');
  });

  it('get the title', function(){
    cy.title().should('include', 'Project4 Recipes')
  });

  // it('check radio elements', () => {
  //   cy.get('input[type="radio"]').not('[disabled]')
  //     .check({ force: true }).should('be.checked')
  // });

  it('click on Recipes', () => {
    cy.get('#add_recipe').click();
  });

  it('click on Categories', () => {
    cy.get('#add_category').click();
  });

  it('click on Ingredients', () => {
    cy.get('#add_ingredient').click();
  });

  it('click on Allergens', () => {
    cy.get('#add_allergen').click();
  });

  // it('can take a screenshot', function(){
  //   cy.screenshot('site', {capture: 'runner'});
  // });

});