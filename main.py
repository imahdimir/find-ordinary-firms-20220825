##

"""

    """

##

import pandas as pd
from mirutil import funcs as mf
from githubdata import GithubData


bt_repo_url = 'https://github.com/imahdimir/d-uniq-BaseTickers'

name = 'name'
btic = 'BaseTicker'

fpn = 'pr.prq'

def main() :
  pass

  ##
  df = pd.read_parquet(fpn)

  ##
  bt_repo = GithubData(bt_repo_url)
  bt_repo.clone()
  ##
  bdfpn = bt_repo.data_filepath
  bdf = pd.read_excel(bdfpn)
  ##
  msk = df[name].isin(bdf[btic])
  df = df[msk]
  ##
  df['group_name'].drop_duplicates()

  ##
  gp2dr = {
      'اوراق بهادار مبتنی بر دارایی فکری' : None ,

      }

  msk = ~ df['group_name'].isin(gp2dr.keys())
  df = df[msk]
  ##
  df = df[['stock_id']]
  ##
  df = df.drop_duplicates()
  ##
  df.to_parquet('ord-firms-ids.prq' , index = False)

  ##
  bt_repo.rmdir()


##

##


##