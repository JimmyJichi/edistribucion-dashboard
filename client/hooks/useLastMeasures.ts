import { gql, useQuery } from "@apollo/client";
import { client } from "../lib/apolloClient";

const QUERY = gql`
  query GetElectricityData($startDate: String!, $endDate: String!) {
    dailyMeasurements(startDate: $startDate, endDate: $endDate) {
      date
      measurements {
        hour
        value
      }
    }
  }
`;

// NOTE: using March 19, 2023 as the date for testing purposes,
// since the API doesn't have data for the current date.
const today = new Date(2023, 2, 19).toISOString().split("T")[0];

export default function useLastMeasures() {
  const { loading, error, data } = useQuery(QUERY, {
    variables: {
      startDate: today,
      endDate: today,
    },
    client: client,
  });

  return { loading, error, data: data?.dailyMeasurements[0].measurements };
}
