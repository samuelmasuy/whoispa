"""Code adapted from zachwill/dom,
Check domain name availability for permutations given an
original word and a default length of the domain name."""
import requests
import simplejson as json
from itertools import permutations
from random import sample
import click


@click.command()
@click.argument('word')
@click.option('--tld', default='com', help="The tld, default is '.com'")
@click.option('--length', type=int, help="The lenght of the domain name")
@click.option('--sample_size', default=20,
              help="The number of results, default is 20.")
def main(word, tld, length, sample_size):
    """Check domain name availability, for a given domain name or permutations
    of its letters."""
    if length:
        candidates = list(permutations(word, length))
        if len(candidates) < sample_size:
            sample_size = len(candidates)
        selected = [''.join(p) for p in sample(candidates, sample_size)]
    else:
        selected = [word]
    for query in selected:
        dom, available = search(query, tld)
        click.echo(dom+": ", nl=False)
        # click.secho(, fg='white')
        if available == 'available':
            click.secho(available, fg='green')
        else:
            click.secho(available, fg='red')


def search(query, tld):
    """Use domainr to get information about domain names."""
    url = "https://domainr.com/api/json/search"
    # query = " ".join(query_domain)
    json_data = requests.get(url, params={'q': query,
                                          'client_id': 'python_zachwill'})
    return parse(json_data.content, tld)


def parse(content, tld):
    """Parse the relevant data from JSON."""
    data = json.loads(content)
    results = data['results']
    for domain in results:
        name = domain['domain']
        if name.endswith("."+tld):
            availability = domain['availability']
            return name, availability


if __name__ == '__main__':
    main()
