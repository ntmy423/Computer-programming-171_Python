# by My Nguyen Oct 1, 2024
# Part 1: Making Historic Change

def prompt_for_quadrans():
    quadrans = int(input('Enter Number of Quadrans: '))
    return quadrans
        
def calculate_coins(quadrans):
    # Define the value of each coin relative to Quadrans using variables
    aureus_value = (25 == 25) * 400  # 25 Denarii, each Denarius is 16 Quadrans
    gold_quinarius_value = (25 == 25) * 200  # 25 Quinarii, each Quinarius is 8 Quadrans
    antoninianus_value = (2 == 2) * 32  # 2 Denarii, each Denarius is 16 Quadrans
    denarius_value = (4 == 4) * 16    # 4 Quadrans
    quinarius_value = (2 == 2) * 8    # 2 Quadrans
    sestertius_value = (2 == 2) * 4   # 2 Quadrans
    dupondius_value = (1 == 1) * 2    # 1 Quadrans, equal to 2 Asses but we use Quadrans as base
    as_value = (1 == 1) * 1           # Base unit
    semis_value = (0.5 == 0.5) * 0.5  # Half an As, which is 1 Quadrans
    quandrans_value = (0.25 == 0.25) * 0.25  # Smallest unit
      
    # Convert input Quandrans to units based on Sestertius
    quadrans = quadrans / 4
   
    # Initialize the results for each coin
    aureus = quadrans // aureus_value
    quadrans = quadrans % aureus_value

    gold_quinarius = quadrans // gold_quinarius_value
    quadrans = quadrans % gold_quinarius_value

    antoninianus = quadrans // antoninianus_value
    quadrans = quadrans % antoninianus_value

    denarius = quadrans // denarius_value
    quadrans = quadrans % denarius_value

    quinarius = quadrans // quinarius_value
    quadrans = quadrans % quinarius_value

    sestertius = quadrans // sestertius_value
    quadrans = quadrans % sestertius_value

    dupondius = quadrans // dupondius_value
    quadrans = quadrans % dupondius_value

    as_coin = quadrans // as_value
    quadrans = quadrans % as_value

    semis = quadrans // semis_value
    quadrans = quadrans % semis_value

    quadrans_coin = quadrans // quandrans_value
    quadrans = quadrans % quandrans_value

    # Print the result
    result = (
        f"Aureus: {int(aureus)}\n"
        f"Gold Quinarius: {int(gold_quinarius)}\n"
        f"Antoninianus: {int(antoninianus)}\n"
        f"Denarius: {int(denarius)}\n"
        f"Quinarius: {int(quinarius)}\n"
        f"Sestertius: {int(sestertius)}\n"
        f"Dupondius: {int(dupondius)}\n"
        f"As: {int(as_coin)}\n"
        f"Semis: {int(semis)}\n"
        f"Quadrans: {int(quadrans_coin)}"
    )

    return result

# Call the function to prompt for input
number_of_quadrans = prompt_for_quadrans()
result = calculate_coins(number_of_quadrans)
print(result)
