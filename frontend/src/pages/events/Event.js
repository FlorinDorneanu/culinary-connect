import React from "react";
import styles from "../../styles/Event.module.css";
import { useCurrentUser } from "../../contexts/CurrentUserContext";
import { Card, Media} from "react-bootstrap";
import { Link } from "react-router-dom";
import Avatar from "../../components/Avatar";


const Event = (props) => {
    const {
        id,
        owner,
        profile_id,
        profile_image,
        description,
        tags,
        category,
        image,
        updated_at,
        event_date,  
        event_time,  
        city,        
        country,
        eventPage,
    } = props;


    const currentUser = useCurrentUser();
    const is_owner = currentUser?.username === owner;

    return (
        <Card className={styles.Event}>
            <Card.Body>
            <Media className="align-items-center justify-content-between">
                <Link to={`/profiles/${profile_id}`}>
                    <Avatar src={profile_image} height={55} />
                    {owner}
                </Link>
                <div className="d-flex align-items-center">
                    <span>{updated_at}</span>
                    {is_owner && eventPage }
                </div>
            </Media>
            </Card.Body>
            <Link to={`/events/${id}`}>
                <Card.Img src={image} alt={description} />
            </Link>
            <Card.Body>
                {description && <Card.Text>{description}</Card.Text>}
                {category && tags &&(
                    <Card.Text className={styles.CategoryTags}>
                        <i className="fa-solid fa-utensils"></i>{category} |
                        <i className="fa-solid fa-tags"></i>{tags}
                    </Card.Text>
                )}
                {event_date && event_time && (
                    <Card.Text className={styles.EventDetail}>
                        <i className="fa-solid fa-calendar-week"></i>{event_date} | {event_time}
                    </Card.Text>
                )}
                {city && country && (
                    <Card.Text className={styles.EventDetail}>
                        <i className="fa-solid fa-map-pin"></i>{city}, {country}
                    </Card.Text>
                )}
            </Card.Body>
        </Card>
    );
};

export default Event;