# $NetBSD$

DISTNAME=	google_cloud_core-2.5.0
PKGNAME=	${PYPKGPREFIX}-${DISTNAME:S/_cloud_/-cloud-/}
CATEGORIES=	net
MASTER_SITES=	${MASTER_SITE_PYPI:=g/google_cloud_core/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/google_cloud_core/
COMMENT=	Google Cloud API client core library
LICENSE=	apache-2.0

DEPENDS+=	${PYPKGPREFIX}-importlib-metadata>=1.0.0:../../devel/py-importlib-metadata
DEPENDS+=	${PYPKGPREFIX}-google-api-core>=2.27.0:../../devel/py-google-api-core
DEPENDS+=	${PYPKGPREFIX}-google-auth>=2.26.1:../../security/py-google-auth

# url2pkg-marker (please do not remove this line.)
.include "../../lang/python/egg.mk"
.include "../../mk/bsd.pkg.mk"
