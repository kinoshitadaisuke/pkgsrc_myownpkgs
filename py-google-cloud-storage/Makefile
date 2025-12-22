# $NetBSD$

DISTNAME=	google_cloud_storage-3.7.0
PKGNAME=	${PYPKGPREFIX}-${DISTNAME:S/_cloud_/-cloud-/}
CATEGORIES=	net
MASTER_SITES=	${MASTER_SITE_PYPI:=g/google_cloud_storage/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/google_cloud_storage/
COMMENT=	Google Cloud Storage API client library
LICENSE=	apache-2.0

DEPENDS+=	${PYPKGPREFIX}-google-auth>=2.26.1:../../security/py-google-auth
DEPENDS+=	${PYPKGPREFIX}-google-api-core>=2.27.0:../../devel/py-google-api-core

# url2pkg-marker (please do not remove this line.)
.include "../../mk/bsd.pkg.mk"
