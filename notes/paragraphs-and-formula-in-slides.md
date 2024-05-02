- Example proposition in network analysis for financial network

  (Acemoglu et al., 2015) - Systemic Risk and Stability in Financial Networks   
  DEFINITION 3: Consider two regular financial networks $\{y_{ij}\}$ and 
  $\{\tilde{y}_{ij}\}$. Conditional on the realization of $p$ negative shocks,
  1.  $\{y_{ij}\}$ is more stable than $\{\tilde{y}_{ij}\}$ if 
      $E_p \, u \geq E_p \,\tilde{u}$, where $E_p$ is the expectation conditional 
      on the realization of $p$ negative shocks.
  2.  $\{y_{ij}\}$ is more resilient than $\{\tilde{y}_{ij}\}$ if 
      $\operatorname{min} u \geq \operatorname{min} \tilde{u}$, where the minimum 
      is taken over all possible realizations of $p$ negative shocks.

  PROPOSITION 3: For a given regular financial netowrk $\{y_{ij}\}$, 
  let $\tilde{y}_{ij} = \beta y_{ij}$ for all $i \neq j$ and some constant 
  $\beta > 1$. Then, financial network $\{\tilde{y}_{ij}\}$ is less stable and 
  resilient than \{y_{ij}\}

  <br>
  (Hledik and Rastelli, 2018) - A dynamic network model to measure exposure diversification in the Austrian interbank market      
  
  __ABSTRACT__  
  We propose a statistical model for weighted temporal networks capable of 
  measuring the level of heterogeneity in a financial system. Our model focuses 
  on the level of diversification of financial institutions; that is, whether 
  they are more inclined to distribute their assets equally among partners, or 
  if they rather concentrate their commitment towards a limited number of 
  institutions. Crucially, a Markov property is introduced to capture time 
  dependencies and to make our measure comparable across time. We apply the 
  model on an original dataset of Austrian interbank exposures. The temporal 
  span encompasses the onset and development of the financial crisis in 2008 
  as well as the beginnings of European sovereign debt crisis in 2011. Our 
  analysis highlights an overall increasing trend for network homogeneity, 
  whereby core banks have a tendency to distribute their market exposures more 
  equally across their partners.
  

- PageRank centrality    
  from (Peña and Touchette, 2012) - A network theory analysis of football strategies  
  $$
   x_i = p \sum_{j \neq i} \frac{A_{ji}}{L_j^\text{out}} x_j + q
  $$
  where $L_j^\text{out} = \sum_k A_{jk}$ is the total number of passes made
  by player $j$, $p$ is a heuristic parameter representing the probability 
  that a player will decide to give the ball away rather than keep it and go 
  for a shot himself, and $q$ is a parameter awarding a 'free' popularity to 
  each player.