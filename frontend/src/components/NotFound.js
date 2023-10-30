import PageNotFound from "../assets/not-found.png";
import Asset from "./Asset";
import styles from "../styles/NotFound.module.css";
import btnStyles from "../styles/Button.module.css";
import { Link } from "react-router-dom";
import { Button, Container } from "react-bootstrap";

const NotFound = () => {
  return (
    <>
      <Container className={`${styles.NotFound}`}>
        <Asset
            src={PageNotFound}
            message={"404 Error. Page Not Found"}
        />
        <Button
            className={`${btnStyles.Button} ${btnStyles.Blue} ${styles.ReturnHome}`}
            as={Link}
            to="/"
        >
            Return Home
        </Button>
      </Container>
    </>
  );
};

export default NotFound;