import generator, output

if __name__ == "__main__":
    app = {
        'name':'SE Yahtzee',
        'author':["Anthony", "Spencer", "Trevin"],
        'license':'MIT',
        'version':"0.0.0"
    }
    
    output.print_project_header(app)
    dice = generator.generate_dice_roll()
    
    print(dice)
    