(function (global) {
    const API_BASE_URL = 'http://localhost:8005';

    function getBrowserInfo() {
        const ua = navigator.userAgent;
        let tem;
        const match = ua.match(/(opera|chrome|safari|firefox|msie|trident(?=\/))\/?\s*(\d+)/i) || [];
        if (/trident/i.test(match[1])) {
            tem = /\brv[ :]+(\d+)/g.exec(ua) || [];
            return { name: 'IE', version: (tem[1] || '') };
        }
        if (match[1] === 'Chrome') {
            tem = ua.match(/\b(OPR|Edge)\/(\d+)/);
            if (tem != null) return { name: tem[1].replace('OPR', 'Opera'), version: tem[2] };
        }
        match[2] = match[2] || navigator.appVersion.match(/version\/(\d+)/i);
        return {
            name: match[1],
            version: match[2] ? match[2][1] : navigator.appVersion,
        };
    }

    function getDeviceType() {
        const ua = navigator.userAgent;
        if (/mobile/i.test(ua)) return 'mobile';
        if (/iPad|Tablet/i.test(ua)) return 'tablet';
        return 'desktop';
    }

    function getOS() {
        const ua = navigator.userAgent;
        if (/windows phone/i.test(ua)) return 'Windows Phone';
        if (/android/i.test(ua)) return 'Android';
        if (/iPad|iPhone|iPod/.test(ua) && !window.MSStream) return 'iOS';
        return 'unknown';
    }

    function getLocation() {
        return new Promise((resolve) => {
            if (!navigator.geolocation) {
                return resolve('unknown');
            }
            navigator.geolocation.getCurrentPosition((position) => {
                const { latitude, longitude } = position.coords;
                resolve({ latitude, longitude });
            }, () => {
                resolve('unknown');
            });
        });
    }

    function createSessionId() {
        return '_' + Math.random().toString(36).substr(2, 9);
    }

    async function assignUserToVariant(data) {
        const response = await fetch(`${API_BASE_URL}/assign`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        });
        return response.json();
    }

    async function determineVariantForUser(experimentId) {
        let sessionId = sessionStorage.getItem('sessionId');
        let variantId = sessionStorage.getItem('variantId');

        if (!sessionId) {
            sessionId = createSessionId();
            sessionStorage.setItem('sessionId', sessionId);
        }

        if (!variantId) {
            const browserInfo = getBrowserInfo();
            const deviceType = getDeviceType();
            const os = getOS();
            const location = await getLocation();

            const userAttributes = {
                hashed_id: sessionId,
                experiment_id: experimentId,
                attributes: {
                    browser: browserInfo.name,
                    browser_version: browserInfo.version,
                    device_type: deviceType,
                    os: os,
                    location: location,
                },
            };

            const assignment = await assignUserToVariant(userAttributes);
            variantId = assignment.assignment.variant_id;
            sessionStorage.setItem('variantId', variantId);
        }

        return { variant_id: variantId };
    }

    global.ExperimentSDK = {
        determineVariantForUser,
    };
})(window);
