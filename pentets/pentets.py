def run():
    rules = load_rules("../rules/*.yml")
    for rule in rules:
        print("Executing rule %s".format(rule.name))
        rule.execute()

if __name__ == '__main__':
    run()
