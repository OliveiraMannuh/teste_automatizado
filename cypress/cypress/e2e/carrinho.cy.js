describe('Carrinho', () => {
    it('Adicionar um item ao carrinho com sucesso', () => {
        //Arrange
            cy.visit('https://saucedemo.com/')

            cy.get('[data-test="username"]').type('standard_user')
            cy.get('[data-test="password"]').type('secret_sauce') 
            cy.get('[data-test="login-button"]').click()

        //Act - Ação
            cy.get('[data-test="add-to-cart-sauce-labs-backpack"]').click()

        //Assert - Validação
            cy.get('.shopping_cart_badge').should('be.visible').and('have.text', '1')

            cy.get('#shopping_cart_container').click()
            cy.contains('Sauce Labs Backpack').should('be.visible')
    })

})