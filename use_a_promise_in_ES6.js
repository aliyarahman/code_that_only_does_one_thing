/* What's this for?:
Say We need an organizer's dashboard to open with a congratulations message if enough houses (over ) have been visited, so the team can plan its weekly activities. When the dashboard loads, it checks with our field metrics database to see if we've met the house visit goal of 1900 and if we want to increase the goal - if not, it should load as normal. But while we're waiting for that information to come back, we want to load other stuff too.
*/


// What we'll get back from the database
const field_metrics = {
    houses_visited: 1903,
    conversations: 1088,
    no_one_home: 1344
};

// For a Promise to work, you will need to write an executor function for it - this lays out how to resolve or reject the promise. It has resolve and reject as parameters/inputs.
const enoughHousesVisited = (resolve, reject) => {
    if (field_metrics.houses_visited > 1900) {
        resolve(`You've met your goal for doorknocking`);
    } else {
        reject('Keep dashboarding as usual!');
    }
};

// Here's where we actually construct the Promise - feeding it the executor function as an input.  
const runDashboardChecks = () => {
    return new Promise(enoughHousesVisited);
}
  

// Write resolve and reject handler functions
const handleSuccess = (resolvedValue) => {
    console.log(resolvedValue);
}

const handleFailure = (rejectionReason) => {
    console.log(rejectionReason);
} 


/* This promise (remember runDashboardChecks returns a Promise object) takes in success/resolve and failure/reject handlers and has two .then()s, to check for rejection first and then move on to handle success.*/
const houseVisitsPromise = runDashboardChecks(field_metrics.houses_visited)
    .then(handleSuccess)
    .catch(handleFailure);