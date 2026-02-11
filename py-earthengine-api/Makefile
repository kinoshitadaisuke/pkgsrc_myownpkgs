# $NetBSD$

DISTNAME=	earthengine_api-1.7.12
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	pkgsrc_myownpkgs python
MASTER_SITES=	${MASTER_SITE_PYPI:=e/earthengine_api/}

MAINTAINER=	INSERT_YOUR_MAIL_ADDRESS_HERE # or use pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/earthengine_api/
COMMENT=	TODO: Short description of the package
#LICENSE=	# TODO: (see mk/license.mk)

# TODO: Extract dependencies from pyproject.toml

USE_LANGUAGES=	# none

DEPENDS+=	${PYPKGPREFIX}-google-cloud-storage>=0:../../pkgsrc_myownpkgs/py-google-cloud-storage
DEPENDS+=	${PYPKGPREFIX}-google-api-python-client>=1.12.1:../../www/py-google-api-python-client
DEPENDS+=	${PYPKGPREFIX}-google-auth>=1.4.1:../../security/py-google-auth
DEPENDS+=	${PYPKGPREFIX}-google-auth-httplib2>=0.0.3:../../security/py-google-auth-httplib2
DEPENDS+=	${PYPKGPREFIX}-httplib2>=0.9.2:../../www/py-httplib2
DEPENDS+=	${PYPKGPREFIX}-requests>=0:../../devel/py-requests
BUILD_DEPENDS+=	${PYPKGPREFIX}-setuptools>=0:../../devel/py-setuptools
DEPENDS+=	${PYPKGPREFIX}-numpy>=0:../../math/py-numpy
DEPENDS+=	${PYPKGPREFIX}-geopandas>=0:../../pkgsrc_myownpkgs/py-geopandas
DEPENDS+=	${PYPKGPREFIX}-absl-py>=0:../../pkgsrc_myownpkgs/py-absl-py

post-install:
	cd ${DESTDIR}${PREFIX}/bin && \
	${MV} earthengine earthengine-${PYVERSSUFFIX} || ${TRUE}

.include "../../math/py-numpy/buildlink3.mk"
.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
